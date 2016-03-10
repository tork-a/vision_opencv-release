Name:           ros-jade-cv-bridge
Version:        1.11.12
Release:        0%{?dist}
Summary:        ROS cv_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/cv_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       opencv-devel
Requires:       opencv-python
Requires:       python-devel
Requires:       ros-jade-rosconsole
Requires:       ros-jade-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  opencv-devel
BuildRequires:  opencv-python
BuildRequires:  python-devel
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs

%description
This contains CvBridge, which converts between ROS Image messages and OpenCV
images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Mar 10 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

* Sun Jan 31 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Sat Jan 16 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Sun Nov 29 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Wed Jul 15 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Wed Dec 31 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.7-0
- Autogenerated by Bloom
