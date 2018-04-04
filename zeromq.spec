Name:           zeromq
Version:        4.2.5
Release:        2%{?dist}
Summary:        Software library for fast, message-based applications

License:        LGPLv3
URL:            http://zeromq.org
Source0:        https://github.com/zeromq/libzmq/releases/download/v%{version}/zeromq-%{version}.tar.gz
Patch0:         zeromq-4.2.5-skip-broken-clang-format.patch

BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openpgm-5.2)
BuildRequires:  cmake >= 2.8.12


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
%patch0 -p1


%build
mkdir Build
pushd Build
%{cmake} \
    -DZEROMQ_CMAKECONFIG_INSTALL_DIR=%{_libdir}/cmake/ZeroMQ \
    -DWITH_OPENPGM=ON \
    -DWITH_LIBSODIUM=ON \
    -DWITH_DOC=OFF ..
make %{?_smp_mflags}
popd


%check
pushd Build
make test
popd


%install
rm -rf %{buildroot}
pushd Build
%make_install
popd

# move pkgconfig to the proper place
mv %{buildroot}/usr/lib/pkgconfig %{buildroot}%{_libdir}
# don't install files twice
rm -f %{buildroot}/usr/share/zmq/*.txt


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/libzmq.pc
%{_libdir}/cmake/*


%files utils
%{_bindir}/*


%changelog
* Wed Apr 04 2018 Jajauma's Packages <jajauma@yandex.ru> - 4.2.5-2
- Rebuild with cmake

* Wed Apr 04 2018 Jajauma's Packages <jajauma@yandex.ru> - 4.2.5-1
- Update to 4.2.5

* Sun Apr 30 2017 Jajauma's Packages <jajauma@yandex.ru> - 4.2.1-2
- Drop OpenPGM support (can't build under MinGW)

* Mon Apr 24 2017 Jajauma's Packages <jajauma@yandex.ru> - 4.2.1-1
- Update to latest upstream release

* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 4.1.5-1
- Public release
