#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : prison
Version  : 5.102.0
Release  : 59
URL      : https://download.kde.org/stable/frameworks/5.102/prison-5.102.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.102/prison-5.102.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.102/prison-5.102.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 MIT
Requires: prison-data = %{version}-%{release}
Requires: prison-lib = %{version}-%{release}
Requires: prison-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qrencode-dev
BuildRequires : zxing-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n prison-5.102.0
cd %{_builddir}/prison-5.102.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673967692
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673967692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/prison
cp %{_builddir}/prison-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/prison/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/prison-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/prison/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/prison-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/prison/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
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
/usr/include/KF5/Prison/Prison/AbstractBarcode
/usr/include/KF5/Prison/Prison/Prison
/usr/include/KF5/Prison/Prison/abstractbarcode.h
/usr/include/KF5/Prison/Prison/prison.h
/usr/include/KF5/Prison/Prison/prison_export.h
/usr/include/KF5/Prison/prison/AbstractBarcode
/usr/include/KF5/Prison/prison/Prison
/usr/include/KF5/Prison/prison/abstractbarcode.h
/usr/include/KF5/Prison/prison/prison.h
/usr/include/KF5/Prison/prison/prison_export.h
/usr/include/KF5/Prison/prison/prison_version.h
/usr/include/KF5/Prison/prison_version.h
/usr/include/KF5/PrisonScanner/Prison/Format
/usr/include/KF5/PrisonScanner/Prison/ScanResult
/usr/include/KF5/PrisonScanner/Prison/VideoScanner
/usr/include/KF5/PrisonScanner/Prison/format.h
/usr/include/KF5/PrisonScanner/Prison/prisonscanner_export.h
/usr/include/KF5/PrisonScanner/Prison/scanresult.h
/usr/include/KF5/PrisonScanner/Prison/videoscanner.h
/usr/lib64/cmake/KF5Prison/KF5PrisonConfig.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonConfigVersion.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Prison/KF5PrisonTargets.cmake
/usr/lib64/libKF5Prison.so
/usr/lib64/libKF5PrisonScanner.so
/usr/lib64/qt5/mkspecs/modules/qt_Prison.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Prison.so.5
/usr/lib64/libKF5Prison.so.5.102.0
/usr/lib64/libKF5PrisonScanner.so.5
/usr/lib64/libKF5PrisonScanner.so.5.102.0
/usr/lib64/qt5/qml/org/kde/prison/libprisonquickplugin.so
/usr/lib64/qt5/qml/org/kde/prison/qmldir
/usr/lib64/qt5/qml/org/kde/prison/scanner/libprisonscannerquickplugin.so
/usr/lib64/qt5/qml/org/kde/prison/scanner/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/prison/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/prison/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/prison/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
