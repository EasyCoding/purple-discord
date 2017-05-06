%global plugin_name discord

%global commit0 28b1aa4cd3028b4884949a8bfb2d86e8feaf58b7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170501

Name: purple-%{plugin_name}
Version: 0
Release: 4.%{date}git%{shortcommit0}%{?dist}
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

%files
%license LICENSE
%doc README.md
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Sat May 06 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20170501git28b1aa4
- Updated to latest snapshot.

* Thu Apr 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20170427gitd879f18
- Updated to latest snapshot.

* Wed Apr 26 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20170426gitcca7860
- Updated to latest snapshot.

* Thu Apr 20 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170420git5c2b3ee
- First SPEC release.
