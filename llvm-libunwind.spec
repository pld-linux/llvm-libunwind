Summary:	LLVM libunwind implementation
Summary(pl.UTF-8):	Implementacja biblioteki libunwind z projektu LLVM
Name:		llvm-libunwind
Version:	14.0.6
Release:	1
License:	BSD-like or MIT
Group:		Libraries
#Source0Download: https://github.com/llvm/llvm-project/releases/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libunwind-%{version}.src.tar.xz
# Source0-md5:	b4ab520fd84066cde664eec95940de59
#Source1Download: https://github.com/llvm/llvm-project/releases/
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxx-%{version}.src.tar.xz
# Source1-md5:	3d5630a8dcbec623172e57fae890351b
#Source2Download: https://github.com/llvm/llvm-project/releases/
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-%{version}.src.tar.xz
# Source2-md5:	80072c6a4be8b9adb60c6aac01f577db
URL:		http://llvm.org/
BuildRequires:	cmake >= 3.13.4
BuildRequires:	libstdc++-devel
BuildRequires:	llvm-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%package static
Summary:	Static LLVM libunwind library
Summary(pl.UTF-8):	Statyczna biblioteka LLVM libunwind
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static LLVM libunwind library.

%description static -l pl.UTF-8
Statyczna biblioteka LLVM libunwind.

%prep
%setup -q -c -a1 -a2

%{__mv} libcxx-%{version}.src libcxx
%{__mv} libunwind-%{version}.src libunwind
%{__mv} llvm-%{version}.src llvm

%build
install -d build
cd build
%cmake ../libunwind

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/llvm-libunwind
cp -p libunwind/include/*.h $RPM_BUILD_ROOT%{_includedir}/llvm-libunwind

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

%files static
%defattr(644,root,root,755)
%{_libdir}/libunwind.a
