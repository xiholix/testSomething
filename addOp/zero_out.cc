#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/shape_interface.h"
#include "tensorflow/core/framework/op_kernel.h"
using namespace tensorflow;

REGISTER_OP("ZeroOut")
.Input("to_zero: int32")
.Output("zeroed: int32")
.SetShapeFn([](::tensorflow::shape_interface::InferenceContext* c){
     c->set_output(0, c->input(0) );
     return Status::OK();
});


class ZeroOutOp: public Opkernel{
public:
    explicit ZeroOutOp(OpkernelConstruction* context):Opkernel(context){}

    void Compute(OpkernelContext* context) override{
        const Tensor&  input_tensor = context->input(0);
        auto input = input_tensor.flat();

        Tensor* output_tensor = NULL;
        OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(), &output_tensor));
        auto output = output_tensor->flat();

        const int N = input.size();
        for(int i=1; i<N; i++){
           output(i) = 0;
        }

        if(N>0)
           output(0) = input(0);
    }

};

REGISTER_KERNEL_BUILDER(Name("ZeroOut").Device(DEVICE_CPU), ZeroOutOp);