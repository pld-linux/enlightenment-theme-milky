%define	_theme	milky
Summary:	Adaption of theme Milk for Mac OS X
Summary(pl.UTF-8):	Adaptacja motywu Milk z Mac OS X
Name:		enlightenment-theme-%{_theme}
Version:	0.9.8.5C
Release:	1
License:	BSD
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/Milky.edj
# Source0-md5:	09cb90c4ed9a8d203073ad5b5be5b31f
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice theme for use with E17 window manager. Milky's theme is inspired
by the work of Max Rudberg. It's an adaptation of his theme Milk for
Mac OS X.

%description -l pl.UTF-8
Przyjemny motyw do używania z zarządcą okien E17. Motyw Milky's został
zainspirowany pracą Maksa Rudberga. Jest to adaptacja jego motywu Milk
dla Mac OS X.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
