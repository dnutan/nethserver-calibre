Name: 			nethserver-calibre
Version: 		0.0.1
Release: 		1%{?dist}
Summary: 		NethServer Calibre Content Server configuration

License: 		GPL
#URL: 			%{url_prefix}/%{name}
Source: 		%{name}-%{version}.tar.gz
#Source1: 		https://releases.mattermost.com/%{mattermost_release}/mattermost-%{mattermost_release}-linux-amd64.tar.gz

BuildRequires:	nethserver-devtools
Requires: 		nethserver-httpd perl wget

BuildArch: 		noarch

%description
NethServer Calibre Content Server configuration

%pre
#if ! getent passwd calibre >/dev/null; then
   # Add the "calibre" user
#   useradd -r -U -s /sbin/nologin -d /var/lib/nethserver/calibre -c "Calibre User" calibre
#fi

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
#rm -rf %{buildroot}
#(cd root; find . -depth -print | cpio -dump %{buildroot})
#mkdir -p %{buildroot}/opt
#tar xvf %{SOURCE1} -C %{buildroot}/opt
mkdir -p %{buildroot}/var/lib/nethserver/calibre/{.config/calibre,libraries}
mkdir -p %{buildroot}/var/log/calibre
%{genfilelist} %{buildroot} \
  --dir /var/lib/nethserver/calibre 'attr(0755,calibre,calibre)' \
  --dir /var/log/calibre 'attr(0755,calibre,calibre)' >  %{name}-%{version}-filelist

cat %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
#%dir /opt/mattermost %attr(0755,mattermost,mattermost)
#%attr(-,mattermost,mattermost) /opt/mattermost/*
#%config /opt/mattermost/config/config.json
%doc COPYING
%doc README.rst
%dir %{_nseventsdir}/%{name}-update
#%dir /opt/calibre

%changelog
* Wed Aug 22 2018 @dnutan <dnutan+gh@mailbox.org> - 0.0.1-1
- Initial Development Release