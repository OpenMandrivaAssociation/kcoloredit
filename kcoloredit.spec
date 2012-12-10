Summary:	Palette files editor
Name:		kcoloredit
Version:	2.0.0
Release:	6
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/
Source0:	%{name}-%{version}-kde4.4.0.tar.bz2
Patch0:		kcoloredit-2.0.0-linkage.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel

%description
KColorEdit is a palette files editor.

It can be used for editing color palettes and for color choosing and naming.

%files -f %{name}.lang
%doc README AUTHORS
%{_kde_bindir}/*
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/%{name}
%{_kde_iconsdir}/*/*/*/*

#------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-kde4.4.0
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

