Summary:        Quick access toolbar for recently used preferences
Summary(pl):    Pasek narzêdziowy szyblkiego dostêpu do najczê¶ciej u¿ywanych ustawieñ
Name:           mozilla-addon-prefbar
Version:        1.0
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:	http://xulplanet.com/downloads/applications/prefbar/prefbar.xpi
Source1:        prefbar-installed-chrome.txt
URL:		http://xulplanet.com/downloads/view.cgi?category=applications&view=prefbar
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	prefbar

%description
%description -l pl
Pasek narzêdziowy szybkiego dostêpu do najczê¶ciej u¿ywanych ustawieñ tj.
pokazywanie obrazków, korzystanie z proxy, w³±czanie Java i JS itd.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
