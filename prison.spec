#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : prison
Version  : 5.49.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.49/prison-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/prison-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/prison-5.49.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: prison-lib
Requires: prison-license
Requires: prison-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qrencode-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: prison-lib
Requires: prison-data
Provides: prison-devel

%description dev
dev components for the prison package.


%package lib
Summary: lib components for the prison package.
Group: Libraries
Requires: prison-data
Requires: prison-license

%description lib
lib components for the prison package.


%package license
Summary: license components for the prison package.
Group: Default

%description license
license components for the prison package.


%prep
%setup -q -n prison-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535436497
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535436497
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/prison
cp LICENSE %{buildroot}/usr/share/doc/prison/LICENSE
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/prison/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/prison.categories

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
/usr/lib64/libKF5Prison.so.5.49.0
/usr/lib64/qt5/qml/org/kde/prison/libprisonquickplugin.so
/usr/lib64/qt5/qml/org/kde/prison/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/prison/LICENSE
/usr/share/doc/prison/cmake_COPYING-CMAKE-SCRIPTS
