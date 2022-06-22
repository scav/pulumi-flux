// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package flux

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func DataInstall(ctx *pulumi.Context, args *DataInstallArgs, opts ...pulumi.InvokeOption) (*DataInstallResult, error) {
	var rv DataInstallResult
	err := ctx.Invoke("flux:index/dataInstall:DataInstall", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking DataInstall.
type DataInstallArgs struct {
	Baseurl            *string  `pulumi:"baseurl"`
	ClusterDomain      *string  `pulumi:"clusterDomain"`
	Components         []string `pulumi:"components"`
	ComponentsExtras   []string `pulumi:"componentsExtras"`
	ImagePullSecrets   *string  `pulumi:"imagePullSecrets"`
	LogLevel           *string  `pulumi:"logLevel"`
	Namespace          *string  `pulumi:"namespace"`
	NetworkPolicy      *bool    `pulumi:"networkPolicy"`
	Registry           *string  `pulumi:"registry"`
	TargetPath         string   `pulumi:"targetPath"`
	TolerationKeys     []string `pulumi:"tolerationKeys"`
	Version            *string  `pulumi:"version"`
	WatchAllNamespaces *bool    `pulumi:"watchAllNamespaces"`
}

// A collection of values returned by DataInstall.
type DataInstallResult struct {
	Baseurl          *string  `pulumi:"baseurl"`
	ClusterDomain    *string  `pulumi:"clusterDomain"`
	Components       []string `pulumi:"components"`
	ComponentsExtras []string `pulumi:"componentsExtras"`
	Content          string   `pulumi:"content"`
	// The provider-assigned unique ID for this managed resource.
	Id                 string   `pulumi:"id"`
	ImagePullSecrets   *string  `pulumi:"imagePullSecrets"`
	LogLevel           *string  `pulumi:"logLevel"`
	Namespace          *string  `pulumi:"namespace"`
	NetworkPolicy      *bool    `pulumi:"networkPolicy"`
	Path               string   `pulumi:"path"`
	Registry           *string  `pulumi:"registry"`
	TargetPath         string   `pulumi:"targetPath"`
	TolerationKeys     []string `pulumi:"tolerationKeys"`
	Version            *string  `pulumi:"version"`
	WatchAllNamespaces *bool    `pulumi:"watchAllNamespaces"`
}

func DataInstallOutput(ctx *pulumi.Context, args DataInstallOutputArgs, opts ...pulumi.InvokeOption) DataInstallResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (DataInstallResult, error) {
			args := v.(DataInstallArgs)
			r, err := DataInstall(ctx, &args, opts...)
			var s DataInstallResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(DataInstallResultOutput)
}

// A collection of arguments for invoking DataInstall.
type DataInstallOutputArgs struct {
	Baseurl            pulumi.StringPtrInput   `pulumi:"baseurl"`
	ClusterDomain      pulumi.StringPtrInput   `pulumi:"clusterDomain"`
	Components         pulumi.StringArrayInput `pulumi:"components"`
	ComponentsExtras   pulumi.StringArrayInput `pulumi:"componentsExtras"`
	ImagePullSecrets   pulumi.StringPtrInput   `pulumi:"imagePullSecrets"`
	LogLevel           pulumi.StringPtrInput   `pulumi:"logLevel"`
	Namespace          pulumi.StringPtrInput   `pulumi:"namespace"`
	NetworkPolicy      pulumi.BoolPtrInput     `pulumi:"networkPolicy"`
	Registry           pulumi.StringPtrInput   `pulumi:"registry"`
	TargetPath         pulumi.StringInput      `pulumi:"targetPath"`
	TolerationKeys     pulumi.StringArrayInput `pulumi:"tolerationKeys"`
	Version            pulumi.StringPtrInput   `pulumi:"version"`
	WatchAllNamespaces pulumi.BoolPtrInput     `pulumi:"watchAllNamespaces"`
}

func (DataInstallOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DataInstallArgs)(nil)).Elem()
}

// A collection of values returned by DataInstall.
type DataInstallResultOutput struct{ *pulumi.OutputState }

func (DataInstallResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataInstallResult)(nil)).Elem()
}

func (o DataInstallResultOutput) ToDataInstallResultOutput() DataInstallResultOutput {
	return o
}

func (o DataInstallResultOutput) ToDataInstallResultOutputWithContext(ctx context.Context) DataInstallResultOutput {
	return o
}

func (o DataInstallResultOutput) Baseurl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.Baseurl }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) ClusterDomain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.ClusterDomain }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) Components() pulumi.StringArrayOutput {
	return o.ApplyT(func(v DataInstallResult) []string { return v.Components }).(pulumi.StringArrayOutput)
}

func (o DataInstallResultOutput) ComponentsExtras() pulumi.StringArrayOutput {
	return o.ApplyT(func(v DataInstallResult) []string { return v.ComponentsExtras }).(pulumi.StringArrayOutput)
}

func (o DataInstallResultOutput) Content() pulumi.StringOutput {
	return o.ApplyT(func(v DataInstallResult) string { return v.Content }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o DataInstallResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v DataInstallResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o DataInstallResultOutput) ImagePullSecrets() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.ImagePullSecrets }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) LogLevel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.LogLevel }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) Namespace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.Namespace }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) NetworkPolicy() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *bool { return v.NetworkPolicy }).(pulumi.BoolPtrOutput)
}

func (o DataInstallResultOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v DataInstallResult) string { return v.Path }).(pulumi.StringOutput)
}

func (o DataInstallResultOutput) Registry() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.Registry }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) TargetPath() pulumi.StringOutput {
	return o.ApplyT(func(v DataInstallResult) string { return v.TargetPath }).(pulumi.StringOutput)
}

func (o DataInstallResultOutput) TolerationKeys() pulumi.StringArrayOutput {
	return o.ApplyT(func(v DataInstallResult) []string { return v.TolerationKeys }).(pulumi.StringArrayOutput)
}

func (o DataInstallResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func (o DataInstallResultOutput) WatchAllNamespaces() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v DataInstallResult) *bool { return v.WatchAllNamespaces }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(DataInstallResultOutput{})
}