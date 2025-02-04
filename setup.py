# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    name='barbican-ui',
    version='0.1',
    summary = 'Barbican User Interface',
    description_file ='README.rst',
    author='OpenStack',
    author_email='openstack-discuss@lists.openstack.org',
    home_page='http://www.openstack.org/',
    classifiers=[
         'Environment :: OpenStack',
         'Intended Audience :: Information Technology',
         'Intended Audience :: System Administrators',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: POSIX :: Linux',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.6'
         'Programming Language :: Python :: 3.8'
    ],
    packages=setuptools.find_packages(exclude=['tests*']),
    include_package_data=True,
    setup_requires=['pbr>=2.0.0'],
    pbr=False)
