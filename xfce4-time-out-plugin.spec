Summary:	Time Out plugin for the Xfce panel
Name:		xfce4-time-out-plugin
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-time-out-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	40f8224097db4a622bb51d22051552fe
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	intltool
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time Out plugin makes it possible to take periodical breaks from the
computer every X minutes. During breaks it locks your screen. It
optionally allows you to postpone breaks for a certain time.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-time-out-plugin
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/panel-plugins/xfce4-time-out-plugin.desktop
