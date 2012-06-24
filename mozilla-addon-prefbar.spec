Summary:	Quick access toolbar for recently used preferences
Summary(pl):	Pasek narz�dziowy szyblkiego dost�pu do najcz�ciej u�ywanych ustawie�
Name:		mozilla-addon-prefbar
%define		_realname	prefbar
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://xulplanet.com/downloads/applications/prefbar/%{_realname}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://xulplanet.com/downloads/view.cgi?category=applications&view=prefbar
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Quick access toolbar for recently used items: showing images, setting
up proxy, enabling Java and JavaScript etc.

%description -l pl
Pasek narz�dziowy szybkiego dost�pu do najcz�ciej u�ywanych ustawie�
tj.  pokazywanie obrazk�w, korzystanie z proxy, w��czanie Java i JS
itd.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
