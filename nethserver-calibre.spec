Name: nethserver-calibre
Version: 0.0.1
Release: 1%{?dist}
Summary: NethServer Calibre Content Server configuration

License: GPL
Source: %{name}-%{version}.tar.gz

BuildRequires: nethserver-devtools
Requires: nethserver-httpd perl wget

BuildArch: noarch

%description
NethServer Calibre Content Server configuration

%prep
%setup -q

%build
#%%{makedocs}
perl createlinks

%install
(cd root; find . -depth -print | cpio -dump %{buildroot})
mkdir -p %{buildroot}/var/lib/nethserver/calibre/{.config/calibre,libraries}
mkdir -p %{buildroot}/var/log/calibre
%{genfilelist} %{buildroot} \
  --dir /var/lib/nethserver/calibre 'attr(0755,calibre,calibre)' \
  --dir /var/log/calibre 'attr(0755,calibre,calibre)' >  %{name}-%{version}-filelist

cat %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%doc README.rst

%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Aug 22 2018 @dnutan <dnutan+gh@mailbox.org> - 0.0.1-1
- Initial Development Release
