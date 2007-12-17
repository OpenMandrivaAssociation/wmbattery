%define name	wmbattery
%define version	2.25
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Battery info docklet for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.kitenet.net/joey/trunk/packages/%{name}-%{version}.tar.bz2
URL:		http://kitenet.net/programs/wmbattery/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRequires:	X11-devel ImageMagick libapm-devel

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
%{__mkdir} -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="WMbattery" longtitle="Battery status docklet" section="System/Monitoring"
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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc TODO README
%doc %{_mandir}/*/*
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name/

