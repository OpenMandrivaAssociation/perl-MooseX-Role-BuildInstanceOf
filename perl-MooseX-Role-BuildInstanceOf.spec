%define upstream_name    MooseX-Role-BuildInstanceOf
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Less Boilerplate when you need lots of Instances
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::MOP)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Iterator)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(Perl6::Junction)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
There can often be a tension between coding for flexibility and for future
growth and writing code that is terse, to the point, and solves the
smallest possible business problem that is brought to you. Writing the
minimum code to solve a particular problem has merit, yet can eventually
leave you with an application that has many hacky modifications and is hard
to test in an isolated manner. Minimum code should not imply minimum
forward planning or poorly tested code.

For me, doing the right thing means I need to both limit myself to the
smallest possible solution for a given business case, yet make sure I am
not writing CODE that is impossible to grow over time in a clean manner.
Generally I attempt to do this by clearly separating the problem domains
under a business case into distinct classes. I then tie all the functional
bits together in the loosest manner possible. the Moose manpage makes this
easy, with its powerful attribute features, type coercions and Roles to
augment classical inheritance.

Loose coupling and deep configurability work well with inversion of control
systems, like the Bread::Board manpage or the IOC built into the the
Catalyst manpage MVC framework. It helps me to defer decisions to the
proper authority and also makes it easier to test my logic, since pieces
are easier to test independently.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


