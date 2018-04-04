Name:           zeromq
Version:        4.2.5
Release:        1%{?dist}
Summary:        Software library for fast, message-based applications

License:        LGPLv3
URL:            http://zeromq.org
Source0:        https://github.com/zeromq/libzmq/releases/download/v%{version}/zeromq-%{version}.tar.gz

BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openpgm-5.2)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  chrpath


%description
The 0MQ lightweight messaging kernel is a library which extends the standard
socket interfaces with features traditionally provided by specialized messaging
middle-ware products. 0MQ sockets provide an abstraction of asynchronous
message queues, multiple messaging patterns, message filtering (subscriptions),
seamless access to multiple transport protocols and more.


%package        devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
Headers and libraries for developing applications that use %{name}
functionality.


%package        utils
Summary:        Utilities shipped with %{name}


%description    utils
%{summary}


%prep
%setup -q


%build
%configure \
    --disable-silent-rules \
    --disable-static \
    --with-libgssapi_krb5 \
    --with-libsodium \
    --with-pgm
make %{?_smp_mflags}


%check
make check


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -delete
chrpath -d %{buildroot}%{_bindir}/*


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libzmq.pc
%{_mandir}/man3/*
%{_mandir}/man7/*


%files utils
%{_bindir}/*


%changelog
* Wed Apr 04 2018 Jajauma's Packages <jajauma@yandex.ru> - 4.2.5-1
- Update to 4.2.5

* Sun Apr 30 2017 Jajauma's Packages <jajauma@yandex.ru> - 4.2.1-2
- Drop OpenPGM support (can't build under MinGW)

* Mon Apr 24 2017 Jajauma's Packages <jajauma@yandex.ru> - 4.2.1-1
- Update to latest upstream release

* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 4.1.5-1
- Public release
