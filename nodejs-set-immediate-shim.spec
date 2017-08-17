%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

# tests disabled due to circular dep, can be enabled later
%global enable_tests 0
%global srcname set-immediate-shim

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.0.1
Release:        6%{?dist}
Summary:        Simple setImmediate shim
License:        MIT
URL:            https://github.com/sindresorhus/set-immediate-shim
Source0:        https://github.com/sindresorhus/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(ava)
BuildRequires:  %{?scl_prefix}npm(require-uncached)
%endif

%description
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf node_modules/

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{srcname}

%changelog
* Fri Jul 07 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-6
- rh-nodejs8-rebuild

* Tue Jan 17 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-5
- Rebuild for RHSCL

* Mon Jun 27 2016 Tom Hughes <tom@compton.nu> - 1.0.1-4
- Update source to actually be 1.0.1 not 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sun Mar  8 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-2
- Update Source0 to comply with github source guidelines
- Move license from %%doc to %%license

* Wed Dec 31 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-1
- Initial package
