Summary:	Quick access toolbar for recently used preferences
Summary(pl):	Pasek narzêdziowy szyblkiego dostêpu do najczê¶ciej u¿ywanych ustawieñ
Name:		mozilla-addon-prefbar
%define		_realname	prefbar
%define		_rc	rc3
Version:	2.3
Release:	0.%{_rc}.3
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/%{_realname}/%{_realname}%{version}%{_rc}.xpi
# Source0-md5:	f6c93ce58408057417cf17cdb18bd59d
Source1:	%{_realname}-installed-chrome.txt
URL:		http://prefbar.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Quick access toolbar for recently used items: showing images, setting
up proxy, enabling Java and JavaScript etc.

%description -l pl
Pasek narzêdziowy szybkiego dostêpu do najczê¶ciej u¿ywanych ustawieñ
tj.  pokazywanie obrazków, korzystanie z proxy, w³±czanie Java i JS
itd.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

mv $RPM_BUILD_ROOT%{_chromedir}/chrome/%{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt ||:
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf} ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome ||:

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf}
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
