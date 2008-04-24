%define version 4.0.2
%define release %mkrel 2
%define oname   kcoloredit

Name:		kde4-kcoloredit
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.kde.org/
Group:		Graphical desktop/KDE
Source0:	%{oname}-%version.tar.bz2
Summary:        Palette files editor
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake >= 2.4.5
BuildRequires:  kdelibs4-devel


%description
KColorEdit is a palette files editor. 
It can be used for editing color palettes and for color 
choosing and naming.

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%{_kde_bindir}/kcoloredit
%{_kde_datadir}/applications/kde4/kcoloredit.desktop
%{_kde_appsdir}/kcoloredit/kcoloreditui.rc
%{_kde_iconsdir}/hicolor/*/apps/kcoloredit.png
%{_kde_datadir}/locale/*/LC_SCRIPTS/*/*

%doc %{_kde_docdir}/HTML/en/doc/index.cache.bz2
%doc %{_kde_docdir}/HTML/en/doc/index.docbook
%doc %{_kde_docdir}/HTML/en/doc/common

#------------------------------------------------

%prep
%setup -q -n %oname-beta5

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
