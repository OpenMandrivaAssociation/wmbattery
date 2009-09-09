%define name	wmbattery
%define version	2.25
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Battery info docklet for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.kitenet.net/joey/trunk/packages/%{name}-%{version}.tar.bz2
URL:		http://kitenet.net/programs/wmbattery/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel imagemagick libapm-devel

%description
wmbattery displays the status of your laptop's battery in a small icon. This
includes if it is plugged in, if the battery is charging, how many minutes of
battery life remain, battery life remaining (with both a percentage and a 
graph), and battery status (high - green, low - yellow, or critical - red).

It works for both ACPI and APM based systems.

%prep
%setup -q

%build
%__autoconf
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%_bindir
%{__mkdir} -p $RPM_BUILD_ROOT/%_mandir/man1
%{__cp} %name $RPM_BUILD_ROOT/%_bindir/
%{__cp} %name.1x $RPM_BUILD_ROOT/%_mandir/man1/

#menu
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=WMbattery
Comment=Battery status docklet
Categories=System;Monitor;
EOF

#icons
%{__mkdir} -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 face.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
%{__mkdir} -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 face.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
%{__mkdir} -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 face.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

# the various states of the applet
%{__mkdir} -p $RPM_BUILD_ROOT/%_iconsdir/%name
%{__cp} *xpm $RPM_BUILD_ROOT/%_iconsdir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name/

