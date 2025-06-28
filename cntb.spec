# Weird go buildsystem not supported by debuginfo
%undefine _debugsource_packages

Name:		cntb
Version:	1.5.5
Release:	1
Source0:	https://github.com/contabo/cntb/archive/refs/tags/v%{version}.tar.gz
# go mod vendor
Source1:	vendor.tar.xz
Summary:	Command line interface for interacting with Contabo Cloud
URL:		https://github.com/contabo/cntb
License:	MIT
Group:		Servers
BuildRequires:	golang

%description
Command line interface for interacting with Contabo Cloud

%prep
%autosetup -p1 -a1 -n cntb-%{version}

%build
go build

%install
mkdir -p %{buildroot}%{_bindir}
mv cntb %{buildroot}%{_bindir}/

%files
%{_bindir}/cntb
