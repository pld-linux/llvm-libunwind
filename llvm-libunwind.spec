Summary:	LLVM libunwind implementation
Summary(pl.UTF-8):	Implementacja biblioteki libunwind z projektu LLVM
Name:		llvm-libunwind
Version:	3.9.1
Release:	1
License:	BSD-like or MIT
Group:		Libraries
Source0:	http://releases.llvm.org/%{version}/libunwind-%{version}.src.tar.xz
# Source0-md5:	f273dd0ed638ad0601b23176a36f187b
URL:		http://llvm.org/
BuildRequires:	cmake >= 3.4.3
BuildRequires:	libstdc++-devel
BuildRequires:	llvm-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LLVM libunwind implementation.

%description -l pl.UTF-8
Implementacja biblioteki libunwind z projektu LLVM.

%package devel
Summary:	Header file for LLVM libunwind implementation
Summary(pl.UTF-8):	Plik nagłówkowy implementacji LLVM libunwind
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for LLVM libunwind implementation.

%description devel -l pl.UTF-8
Plik nagłówkowy implementacji LLVM libunwind.

%prep
%setup -q -n libunwind-%{version}.src

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/llvm-libunwind
cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}/llvm-libunwind

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunwind.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libunwind.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunwind.so
%{_includedir}/llvm-libunwind
