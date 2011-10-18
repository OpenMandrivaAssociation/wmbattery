Name: 	 	wmbattery
Summary: 	Battery info docklet for WindowMaker
Version: 	2.40
Release: 	2

Source: 	%{name}-%{version}.tar.xz
URL:		http://kitenet.net/programs/wmbattery/
License:	GPL
Group:		Graphical desktop/WindowMaker

BuildRequires:	libx11-devel
BuildRequires:	imagemagick
BuildRequires:	libapm-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel

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

