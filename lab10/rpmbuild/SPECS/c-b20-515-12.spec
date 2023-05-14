Name:       c-b20-515-12
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Плотникова Р.В. группы Б20-515
Group:      Testing
License:    GPL
URL:        https://github.com/TechnoStrife/OSS_LABS
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b20-515-12 c-b20-515-12.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b20-515-12 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b20-515-12-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b20-515-12

%changelog
* Fri May 12 2023 Roschin
- Added %{_bindir}/c-b20-515-12
