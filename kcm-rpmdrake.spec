Name:           kcm-rpmdrake
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching Rpmdrake
Version:        1.0
Release:        14
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

%description
Rpmdrake launcher for KDE Control Center

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build 

%files
%defattr(-,root,root)
%doc
%{_datadir}/kde4/services/kcm_rpmdrake.desktop

