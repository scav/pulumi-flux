# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'DataSyncResult',
    'AwaitableDataSyncResult',
    'data_sync',
    'data_sync_output',
]

@pulumi.output_type
class DataSyncResult:
    """
    A collection of values returned by DataSync.
    """
    def __init__(__self__, branch=None, commit=None, content=None, git_implementation=None, id=None, interval=None, kustomize_content=None, kustomize_path=None, name=None, namespace=None, patch_file_paths=None, patch_names=None, path=None, secret=None, semver=None, tag=None, target_path=None, url=None):
        if branch and not isinstance(branch, str):
            raise TypeError("Expected argument 'branch' to be a str")
        pulumi.set(__self__, "branch", branch)
        if commit and not isinstance(commit, str):
            raise TypeError("Expected argument 'commit' to be a str")
        pulumi.set(__self__, "commit", commit)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if git_implementation and not isinstance(git_implementation, str):
            raise TypeError("Expected argument 'git_implementation' to be a str")
        pulumi.set(__self__, "git_implementation", git_implementation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interval and not isinstance(interval, int):
            raise TypeError("Expected argument 'interval' to be a int")
        pulumi.set(__self__, "interval", interval)
        if kustomize_content and not isinstance(kustomize_content, str):
            raise TypeError("Expected argument 'kustomize_content' to be a str")
        pulumi.set(__self__, "kustomize_content", kustomize_content)
        if kustomize_path and not isinstance(kustomize_path, str):
            raise TypeError("Expected argument 'kustomize_path' to be a str")
        pulumi.set(__self__, "kustomize_path", kustomize_path)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if patch_file_paths and not isinstance(patch_file_paths, dict):
            raise TypeError("Expected argument 'patch_file_paths' to be a dict")
        pulumi.set(__self__, "patch_file_paths", patch_file_paths)
        if patch_names and not isinstance(patch_names, list):
            raise TypeError("Expected argument 'patch_names' to be a list")
        pulumi.set(__self__, "patch_names", patch_names)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if secret and not isinstance(secret, str):
            raise TypeError("Expected argument 'secret' to be a str")
        pulumi.set(__self__, "secret", secret)
        if semver and not isinstance(semver, str):
            raise TypeError("Expected argument 'semver' to be a str")
        pulumi.set(__self__, "semver", semver)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if target_path and not isinstance(target_path, str):
            raise TypeError("Expected argument 'target_path' to be a str")
        pulumi.set(__self__, "target_path", target_path)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def branch(self) -> Optional[str]:
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter
    def commit(self) -> Optional[str]:
        return pulumi.get(self, "commit")

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="gitImplementation")
    def git_implementation(self) -> Optional[str]:
        return pulumi.get(self, "git_implementation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def interval(self) -> Optional[int]:
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="kustomizeContent")
    def kustomize_content(self) -> str:
        return pulumi.get(self, "kustomize_content")

    @property
    @pulumi.getter(name="kustomizePath")
    def kustomize_path(self) -> str:
        return pulumi.get(self, "kustomize_path")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="patchFilePaths")
    def patch_file_paths(self) -> Mapping[str, str]:
        return pulumi.get(self, "patch_file_paths")

    @property
    @pulumi.getter(name="patchNames")
    def patch_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "patch_names")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def secret(self) -> Optional[str]:
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def semver(self) -> Optional[str]:
        return pulumi.get(self, "semver")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter(name="targetPath")
    def target_path(self) -> str:
        return pulumi.get(self, "target_path")

    @property
    @pulumi.getter
    def url(self) -> str:
        return pulumi.get(self, "url")


class AwaitableDataSyncResult(DataSyncResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return DataSyncResult(
            branch=self.branch,
            commit=self.commit,
            content=self.content,
            git_implementation=self.git_implementation,
            id=self.id,
            interval=self.interval,
            kustomize_content=self.kustomize_content,
            kustomize_path=self.kustomize_path,
            name=self.name,
            namespace=self.namespace,
            patch_file_paths=self.patch_file_paths,
            patch_names=self.patch_names,
            path=self.path,
            secret=self.secret,
            semver=self.semver,
            tag=self.tag,
            target_path=self.target_path,
            url=self.url)


def data_sync(branch: Optional[str] = None,
              commit: Optional[str] = None,
              git_implementation: Optional[str] = None,
              interval: Optional[int] = None,
              name: Optional[str] = None,
              namespace: Optional[str] = None,
              patch_names: Optional[Sequence[str]] = None,
              secret: Optional[str] = None,
              semver: Optional[str] = None,
              tag: Optional[str] = None,
              target_path: Optional[str] = None,
              url: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableDataSyncResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['branch'] = branch
    __args__['commit'] = commit
    __args__['gitImplementation'] = git_implementation
    __args__['interval'] = interval
    __args__['name'] = name
    __args__['namespace'] = namespace
    __args__['patchNames'] = patch_names
    __args__['secret'] = secret
    __args__['semver'] = semver
    __args__['tag'] = tag
    __args__['targetPath'] = target_path
    __args__['url'] = url
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('flux:index/dataSync:DataSync', __args__, opts=opts, typ=DataSyncResult).value

    return AwaitableDataSyncResult(
        branch=__ret__.branch,
        commit=__ret__.commit,
        content=__ret__.content,
        git_implementation=__ret__.git_implementation,
        id=__ret__.id,
        interval=__ret__.interval,
        kustomize_content=__ret__.kustomize_content,
        kustomize_path=__ret__.kustomize_path,
        name=__ret__.name,
        namespace=__ret__.namespace,
        patch_file_paths=__ret__.patch_file_paths,
        patch_names=__ret__.patch_names,
        path=__ret__.path,
        secret=__ret__.secret,
        semver=__ret__.semver,
        tag=__ret__.tag,
        target_path=__ret__.target_path,
        url=__ret__.url)


@_utilities.lift_output_func(data_sync)
def data_sync_output(branch: Optional[pulumi.Input[Optional[str]]] = None,
                     commit: Optional[pulumi.Input[Optional[str]]] = None,
                     git_implementation: Optional[pulumi.Input[Optional[str]]] = None,
                     interval: Optional[pulumi.Input[Optional[int]]] = None,
                     name: Optional[pulumi.Input[Optional[str]]] = None,
                     namespace: Optional[pulumi.Input[Optional[str]]] = None,
                     patch_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     secret: Optional[pulumi.Input[Optional[str]]] = None,
                     semver: Optional[pulumi.Input[Optional[str]]] = None,
                     tag: Optional[pulumi.Input[Optional[str]]] = None,
                     target_path: Optional[pulumi.Input[str]] = None,
                     url: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[DataSyncResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
