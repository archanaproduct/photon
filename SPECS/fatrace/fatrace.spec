Summary:	fatrace reports file access events from all running processes.
Name:		fatrace
Version:	0.15
Release:	1%{?dist}
License:	GNU GPLv3
URL:		https://launchpad.net/fatrace
Source0:	https://launchpad.net/fatrace/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
%define sha1 fatrace=2740cff5fd8d0cc230a41c018ab651066e5d5d1f
Requires:	python3
Group:		Utilities
Vendor:		VMware, Inc.
Distribution:   Photon

%description
fatrace reports file access events from all running processes.
Its main purpose is to find processes which keep waking up the disk unnecessarily and thus prevent some power saving.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -vdm 755 %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/*

%changelog
*   Wed Sep 09 2020 Gerrit Photon <photon-checkins@vmware.com> 0.15-1
-   Automatic Version Bump
*   Tue Jun 23 2020 Tapas Kundu <tkundu@vmware.com> 0.13-2
-   Require python3
*   Thu Sep 20 2018 Sujay G <gsujay@vmware.com> 0.13-1
-   Bump fatrace version to 0.13
*   Fri Mar 24 2017 Alexey Makhalov <amakhalov@vmware.com> 0.12-2
-   Added fatrace-sysmacros.patch to fix build issue with glibc-2.25
*   Mon Feb 6 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.12-1
-   initial version
