Summary:	Time Out plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka upływu czasu dla panelu Xfce
Name:		xfce4-time-out-plugin
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-time-out-plugin/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	12ce48686ef55789e1e14523ec62862a
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-time-out-plugin
BuildRequires:	glib2-devel >= 2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libtime-out.so
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/panel/plugins/xfce4-time-out-plugin.desktop
