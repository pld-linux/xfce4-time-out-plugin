Summary:	Time Out plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka upływu czasu dla panelu Xfce
Name:		xfce4-time-out-plugin
Version:	1.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	2fef9fbcc9791de30bcceecfde92d4c3
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	glib2-devel >= 2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time Out plugin makes it possible to take periodical breaks from the
computer every X minutes. During breaks it locks your screen. It
optionally allows you to postpone breaks for a certain time.

%description -l pl.UTF-8
Wtyczka Time Out umożliwia robienie regularnych przerw od komputera co
każde X minut. W czasie przerw blokuje ekran. Opcjonalnie pozwala
odłożyć przerwy na określony czas.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libtime-out.so
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/panel/plugins/xfce4-time-out-plugin.desktop
