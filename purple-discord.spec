%global plugin_name discord

%global commit0 5c2b3ee78ed4615636b8a80462e8c3a7541bfd6c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170420

Name: purple-%{plugin_name}
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}
Summary: Discord plugin for libpurple

License: GPLv3+
URL: https://github.com/EionRobb/purple-discord
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Discord protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Discord to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Discord protocol implemented by
purple-discord.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license LICENSE
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Thu Apr 20 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170420git5c2b3ee
- First SPEC release.
