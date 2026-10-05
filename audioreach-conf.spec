%global debug_package %{nil}
%global release_num 2

Name:           audioreach-conf
Version:        1.1.0
Release:        %{release_num}%{?dist}
Summary:        AudioReach configuration files
License:        BSD-3-Clause
URL:            https://github.com/AudioReach/audioreach-conf
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        acdbdata/acdb_cal.acdb
Source2:        acdbdata/workspaceFileXml.qwsp

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig

%description
Provides vendor-, chipset-, and board-specific configuration data used by
AudioReach components, including topology and calibration key-value
definitions for audio use cases.

This build enables the Qualcomm (--with-qcom) configuration set, which
installs ACDB calibration data and card-definition XML files for the
following chipsets:
  qcm6490, qcs615, qcs8275, qcs8300, qcs9075, qcs9100, sm8750,
  GLYMUR, Kaanapali, MAHUA, X1E80100.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --with-qcom

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Workaround: override qcm6490 acdb to remove ECNS-v2 and CFCM modules; suspected SPF/FastRPC issue
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/acdbdata/QCS6490_RB3Gen2/acdb_cal.acdb
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/acdbdata/QCS6490_RB3Gen2/workspaceFileXml.qwsp
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/acdbdata/QCM6490_IDP/acdb_cal.acdb
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/acdbdata/QCM6490_IDP/workspaceFileXml.qwsp

%files
%license LICENSE
# Header installed by qcom/Makefile.am (kvh2xml_include_HEADERS)
%{_includedir}/kvh2xml.h

# pkg-config files
%{_libdir}/pkgconfig/kvh2xml.pc
%{_libdir}/pkgconfig/config.pc

# ---- qcm6490 ----
%dir %{_sysconfdir}/acdbdata/QCS6490_RB3Gen2
%{_sysconfdir}/acdbdata/QCS6490_RB3Gen2/acdb_cal.acdb
%{_sysconfdir}/acdbdata/QCS6490_RB3Gen2/workspaceFileXml.qwsp
%dir %{_sysconfdir}/acdbdata/QCM6490_IDP
%{_sysconfdir}/acdbdata/QCM6490_IDP/acdb_cal.acdb
%{_sysconfdir}/acdbdata/QCM6490_IDP/workspaceFileXml.qwsp

# ---- qcs615 ----
%dir %{_sysconfdir}/acdbdata/TALOS_EVK
%{_sysconfdir}/acdbdata/TALOS_EVK/acdb_cal.acdb
%{_sysconfdir}/acdbdata/TALOS_EVK/workspaceFileXml.qwsp

# ---- qcs8275 ----
%dir %{_sysconfdir}/acdbdata/MONACO_EVK
%{_sysconfdir}/acdbdata/MONACO_EVK/acdb_cal.acdb
%{_sysconfdir}/acdbdata/MONACO_EVK/workspaceFileXml.qwsp

# ---- qcs8300 ----
%dir %{_sysconfdir}/acdbdata/qcs8300
%{_sysconfdir}/acdbdata/qcs8300/acdb_cal.acdb
%{_sysconfdir}/acdbdata/qcs8300/workspaceFileXml.qwsp

# ---- qcs9075 ----
%dir %{_sysconfdir}/acdbdata/LEMANS_EVK
%{_sysconfdir}/acdbdata/LEMANS_EVK/acdb_cal.acdb
%{_sysconfdir}/acdbdata/LEMANS_EVK/workspaceFileXml.qwsp

# ---- qcs9100 ----
%dir %{_sysconfdir}/acdbdata/qcs9100
%{_sysconfdir}/acdbdata/qcs9100/acdb_cal.acdb
%{_sysconfdir}/acdbdata/qcs9100/workspaceFileXml.qwsp

# ---- sm8750 ----
%dir %{_sysconfdir}/acdbdata/SM8750_MTP
%{_sysconfdir}/acdbdata/SM8750_MTP/acdb_cal.acdb
%{_sysconfdir}/acdbdata/SM8750_MTP/workspaceFileXml.qwsp

# ---- GLYMUR ----
%dir %{_sysconfdir}/acdbdata/GLYMUR
%{_sysconfdir}/acdbdata/GLYMUR/acdb_cal.acdb
%{_sysconfdir}/acdbdata/GLYMUR/workspaceFileXml.qwsp

# ---- Kaanapali ----
%dir %{_sysconfdir}/acdbdata/Kaanapali
%{_sysconfdir}/acdbdata/Kaanapali/acdb_cal.acdb
%{_sysconfdir}/acdbdata/Kaanapali/workspaceFileXml.qwsp

# ---- MAHUA ----
%dir %{_sysconfdir}/acdbdata/MAHUA
%{_sysconfdir}/acdbdata/MAHUA/acdb_cal.acdb
%{_sysconfdir}/acdbdata/MAHUA/workspaceFileXml.qwsp

# ---- X1E80100 ----
%dir %{_sysconfdir}/acdbdata/X1E80100
%{_sysconfdir}/acdbdata/X1E80100/acdb_cal.acdb
%{_sysconfdir}/acdbdata/X1E80100/workspaceFileXml.qwsp

# card-defs.xml is installed to $(sysconfdir) — last board's install wins
%{_sysconfdir}/card-defs.xml

%changelog
* Mon Oct 05 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 1.1.0-2
- qcm6490: override acdb to remove ECNS-v2 and CFCM modules as workaround for deep buffer playback/record failure

* Thu Aug 14 2026 Qualcomm Linux <quic_linux@quicinc.com> - 1.1.0-1
- Initial RPM packaging of audioreach-conf version 1.1.0
