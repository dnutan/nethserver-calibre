Name: nethserver-calibre
Version: 0.0.2
Release: 1%{?dist}
Summary: NethServer Calibre Content Server configuration

License: GPLv3
URL: https://github.com/dnutan/%{name}
Source: %{name}-%{version}.tar.gz

BuildRequires: nethserver-devtools
Requires: perl
Requires: python2
Requires: nethserver-httpd wget

BuildArch: noarch

%description
NethServer Calibre Content Server configuration

#%pre
#if ! getent passwd calibre >/dev/null; then
   # Add the "calibre" user
#   useradd -r -U -s /sbin/nologin -d /var/lib/nethserver/calibre -c "Calibre User" calibre
#fi

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
#rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
# mkdir -p %{buildroot}/var/lib/nethserver/calibre/{.config/calibre,libraries}
# mkdir -p %{buildroot}/var/log/calibre
%{genfilelist} %{buildroot} >  %{name}-%{version}-filelist
#%{genfilelist} %{buildroot} \
#%{genfilelist} %{buildroot} \
#  --dir /var/lib/nethserver/calibre \
#  --dir /var/log/calibre >  %{name}-%{version}-filelist
#  --dir /var/lib/nethserver/calibre 'attr(0755,calibre,calibre)' \
#  --dir /var/log/calibre 'attr(0755,calibre,calibre)' >  %{name}-%{version}-filelist

cat %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%license COPYING
#%%doc README.rst

%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Aug 22 2018 @dnutan <dnutan+gh@mailbox.org> - 0.0.1-1.ns7
- Initial Development Release

* Sun Sep 01 2018 @dnutan <dnutan+gh@mailbox.org> - 0.0.2-1.ns7
- split db
- refactor handling of calibre libraries