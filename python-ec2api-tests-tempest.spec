%{!?upstream_version: %global upstream_version %{commit}}
%global commit ba836d429f38ce0831cf336feb2a620fdcf3efcb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service ec2api
%global plugin ec2api-tempest-plugin
%global module ec2api_tempest_plugin

%if 0%{?fedora}
# Disabling Python3 subpackage as ec2api tempest plugin is not ready for python3
%global with_python3 0
%endif

%global common_desc \
This package contains Tempest tests to cover the EC2 API project. \
Additionally it provides a plugin to automatically load these \
tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    0.1.0
Release:    1%{?alphatag}%{?dist}
Summary:    Tempest Integration of EC2-API Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

BuildArch:  noarch

BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Obsoletes:   python-ec2-api-tests < 5.1.0

Requires:   python2-tempest >= 1:18.0.0
Requires:   python2-pbr >= 3.1.1
Requires:   python2-oslo-config >= 2:5.2.0
Requires:   python2-oslo-log >= 3.36.0
Requires:   python2-botocore
Requires:   python2-testtools
Requires:   python2-six => 1.10.0
%if 0%{?fedora} > 0
Requires:   python2-lxml
%else
Requires:   python-lxml
%endif
Requires:   python2-netaddr
Requires:   python2-paramiko

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-pbr >= 3.1.1
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-botocore
Requires:   python3-testtools
Requires:   python3-six => 1.10.0
Requires:   python3-lxml
Requires:   python3-netaddr
Requires:   python3-paramiko

%description -n python3-%{service}-tests-tempest
%{common_desc}
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info
%endif

%changelog
* Mon Aug 27 2018 RDO <dev@lists.rdoproject.org> 0.1.0-1.ba836d4git
- Update to 0.1.0

* Thu Aug 23 2018 Chandan Kumar <chkumar@redhat.com> 0.0.1-0.2.ba836d42git
- Update to pre-release 0.0.1 (ba836d429f38ce0831cf336feb2a620fdcf3efcb)
