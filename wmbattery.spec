Name: 	 	wmbattery
Summary: 	Battery info docklet for WindowMaker
Version: 	2.40
Release: 	2

Source: 	%{name}-%{version}.tar.xz
URL:		http://kitenet.net/programs/wmbattery/
License:	GPL
Group:		Graphical desktop/WindowMaker

BuildRequires:	pkgconfig(x11)
BuildRequires:	imagemagick
BuildRequires:	libapm-devel
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

%description
wmbattery displays the status of your laptop's battery in a small icon. This
includes if it is plugged in, if the battery is charging, how many minutes of
battery life remain, battery life remaining (with both a percentage and a 
graph), and battery status (high - green, low - yellow, or critical - red).

It works for both ACPI and APM based systems.

%prep
%setup -q

%build
sed -i \
	-e '/^icondir/s:icons:pixmaps:' \
	-e '/^USE_HAL/d' \
	autoconf/makeinfo.in

autoconf
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

#menu
%{__mkdir} -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=WMbattery
Comment=Battery status docklet
Categories=System;Monitor;
EOF

#icons
convert -size 48x48 face.xpm %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc TODO README
%doc %{_mandir}/*/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}/*.xpm



%changelog
* Wed Oct 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.40-2
+ Revision: 705326
- new version 2.40
  cleaned up spec
  removed hal linking

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.25-6
+ Revision: 634774
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.25-5mdv2010.0
+ Revision: 434773
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.25-4mdv2009.0
+ Revision: 262014
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.25-3mdv2009.0
+ Revision: 256040
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.25-1mdv2008.1
+ Revision: 135500
- fix directory creation
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import wmbattery


* Fri Apr 14 2006 Udo Rader <udo.rader@bestsolution.at> 2.25-1mdk
- new upstream version

* Tue Nov 01 2005 Austin Acton <austin@mandriva.org> 2.22-1mdk
- from Udo Rader <udo.rader@bestsolution.at> :
  - new upstream version

* Mon Mar 21 2005 Austin Acton <austin@mandrake.org> 2.20-1mdk
- from Udo Rader <udo.rader@bestsolution.at> :
  - initial version
