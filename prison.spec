#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : prison
Version  : 5.75.0
Release  : 33
URL      : https://download.kde.org/stable/frameworks/5.75/prison-5.75.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.75/prison-5.75.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.75/prison-5.75.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: prison-data = %{version}-%{release}
Requires: prison-lib = %{version}-%{release}
Requires: prison-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qrencode-dev
BuildRequires : qtbase-dev mesa-dev

%description
# Prison
A barcode abstraction layer providing uniform access to generation of barcodes with data

%package data
Summary: data components for the prison package.
Group: Data

%description data
data components for the prison package.


%package dev
Summary: dev components for the prison package.
Group: Development
Requires: prison-lib = %{version}-%{release}
Requires: prison-data = %{version}-%{release}
Provides: prison-devel = %{version}-%{release}
Requires: prison = %{version}-%{release}

%description dev
dev components for the prison package.


%package lib
Summary: lib components for the prison package.
Group: Libraries
Requires: prison-data = %{version}-%{release}
Requires: prison-license = %{version}-%{release}

%description lib
lib components for the prison package.


%package license
Summary: license components for the prison package.
Group: Default

%description license
license components for the prison package.


%prep
%setup -q -n prison-5.75.0
cd %{_builddir}/prison-5.75.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602633500
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602633500
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/prison
cp %{_builddir}/prison-5.75.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/prison/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/prison-5.75.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/prison/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/prison.categories
/usr/share/qlogging-categories5/prison.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/prison/AbstractBarcode
/usr/include/KF5/prison/Prison
/usr/include/KF5/prison/abstractbarcode.h
/usr/include/KF5/prison/prison.h
/usr/include/KF5/prison/prison_export.h
/usr/include/KF5/prison_version.h
/usr/lib64/cmake/KF5Prison/KF5PrisonConfig.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonConfigVersion.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonTargets.cmake
/usr/lib64/libKF5Prison.so
/usr/lib64/qt5/mkspecs/modules/qt_Prison.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Prison.so.5
/usr/lib64/libKF5Prison.so.5.75.0
/usr/lib64/qt5/qml/org/kde/prison/libprisonquickplugin.so
/usr/lib64/qt5/qml/org/kde/prison/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/prison/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/prison/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
