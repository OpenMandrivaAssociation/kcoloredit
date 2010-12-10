%define version 2.0.0
%define release %mkrel 5
%define oname   kcoloredit

Name:		kcoloredit
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.kde.org/
Group:		Graphical desktop/KDE
Source0:	%{oname}-%version-kde4.3.1.tar.bz2
Summary:        Palette files editor
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake >= 2.4.5
BuildRequires:  kdelibs4-devel
Obsoletes:	kde4-%name < 4.0.3
Conflicts:	kde-l10n < 3.5.9-5
%if %mdkversion < 200900
Obsoletes:	kdegraphics-kcoloredit < 1:3.5.10-3
%endif
%if %mdkversion < 200100
Obsoletes:  kdegraphics3-kcoloredit < 1:3.5.10-5
%endif

%description
KColorEdit is a palette files editor. 
It can be used for editing color palettes and for color 
choosing and naming.

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#------------------------------------------------

%prep
%setup -q -n %name-%version-kde4.3.1

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}
cd -
%find_lang %name --with-html

%clean
rm -rf %buildroot
