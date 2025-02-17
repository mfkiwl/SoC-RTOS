```
code
├── controller
│   ├── FNN
│   │   ├── convolutional
│   │   │   └── ntm_controller.psl
│   │   └── standard
│   │       └── ntm_controller.psl
│   ├── LSTM
│   │   ├── convolutional
│   │   │   ├── ntm_activation_gate_vector.psl
│   │   │   ├── ntm_controller.psl
│   │   │   ├── ntm_forget_gate_vector.psl
│   │   │   ├── ntm_hidden_gate_vector.psl
│   │   │   ├── ntm_input_gate_vector.psl
│   │   │   ├── ntm_output_gate_vector.psl
│   │   │   └── ntm_state_gate_vector.psl
│   │   └── standard
│   │       ├── ntm_activation_gate_vector.psl
│   │       ├── ntm_controller.psl
│   │       ├── ntm_forget_gate_vector.psl
│   │       ├── ntm_hidden_gate_vector.psl
│   │       ├── ntm_input_gate_vector.psl
│   │       ├── ntm_output_gate_vector.psl
│   │       └── ntm_state_gate_vector.psl
│   └── transformer
│       ├── components
│       │   ├── ntm_masked_multi_head_attention.psl
│       │   ├── ntm_masked_scaled_dot_product_attention.psl
│       │   ├── ntm_multi_head_attention.psl
│       │   └── ntm_scaled_dot_product_attention.psl
│       ├── fnn
│       │   └── ntm_fnn.psl
│       ├── functions
│       │   ├── ntm_layer_norm.psl
│       │   └── ntm_positional_encoding.psl
│       ├── inputs
│       │   ├── ntm_inputs_vector.psl
│       │   ├── ntm_keys_vector.psl
│       │   ├── ntm_queries_vector.psl
│       │   └── ntm_values_vector.psl
│       ├── lstm
│       │   ├── ntm_activation_gate_vector.psl
│       │   ├── ntm_forget_gate_vector.psl
│       │   ├── ntm_hidden_gate_vector.psl
│       │   ├── ntm_input_gate_vector.psl
│       │   ├── ntm_lstm.psl
│       │   ├── ntm_output_gate_vector.psl
│       │   └── ntm_state_gate_vector.psl
│       └── top
│           ├── ntm_controller.psl
│           ├── ntm_decoder.psl
│           └── ntm_encoder.psl
├── dnc
│   ├── memory
│   │   ├── dnc_addressing.psl
│   │   ├── dnc_allocation_weighting.psl
│   │   ├── dnc_backward_weighting.psl
│   │   ├── dnc_forward_weighting.psl
│   │   ├── dnc_matrix_content_based_addressing.psl
│   │   ├── dnc_memory_matrix.psl
│   │   ├── dnc_memory_retention_vector.psl
│   │   ├── dnc_precedence_weighting.psl
│   │   ├── dnc_read_content_weighting.psl
│   │   ├── dnc_read_vectors.psl
│   │   ├── dnc_read_weighting.psl
│   │   ├── dnc_sort_vector.psl
│   │   ├── dnc_temporal_link_matrix.psl
│   │   ├── dnc_usage_vector.psl
│   │   ├── dnc_vector_content_based_addressing.psl
│   │   ├── dnc_write_content_weighting.psl
│   │   └── dnc_write_weighting.psl
│   ├── top
│   │   ├── dnc_interface_matrix.psl
│   │   ├── dnc_interface_top.psl
│   │   ├── dnc_interface_vector.psl
│   │   ├── dnc_output_vector.psl
│   │   └── dnc_top.psl
│   └── trained
│       └── dnc_trained_top.psl
├── math
│   ├── algebra
│   │   ├── matrix
│   │   │   ├── ntm_matrix_convolution.psl
│   │   │   ├── ntm_matrix_inverse.psl
│   │   │   ├── ntm_matrix_multiplication.psl
│   │   │   ├── ntm_matrix_product.psl
│   │   │   ├── ntm_matrix_summation.psl
│   │   │   ├── ntm_matrix_transpose.psl
│   │   │   ├── ntm_matrix_vector_convolution.psl
│   │   │   ├── ntm_matrix_vector_product.psl
│   │   │   └── ntm_transpose_vector_product.psl
│   │   ├── scalar
│   │   │   ├── ntm_scalar_multiplication.psl
│   │   │   └── ntm_scalar_summation.psl
│   │   ├── tensor
│   │   │   ├── ntm_tensor_convolution.psl
│   │   │   ├── ntm_tensor_inverse.psl
│   │   │   ├── ntm_tensor_matrix_convolution.psl
│   │   │   ├── ntm_tensor_matrix_product.psl
│   │   │   ├── ntm_tensor_multiplication.psl
│   │   │   ├── ntm_tensor_product.psl
│   │   │   ├── ntm_tensor_summation.psl
│   │   │   └── ntm_tensor_transpose.psl
│   │   └── vector
│   │       ├── ntm_dot_product.psl
│   │       ├── ntm_vector_convolution.psl
│   │       ├── ntm_vector_cosine_similarity.psl
│   │       ├── ntm_vector_module.psl
│   │       ├── ntm_vector_multiplication.psl
│   │       └── ntm_vector_summation.psl
│   ├── calculus
│   │   ├── matrix
│   │   │   ├── ntm_matrix_differentiation.psl
│   │   │   ├── ntm_matrix_integration.psl
│   │   │   └── ntm_matrix_softmax.psl
│   │   ├── tensor
│   │   │   ├── ntm_tensor_differentiation.psl
│   │   │   ├── ntm_tensor_integration.psl
│   │   │   └── ntm_tensor_softmax.psl
│   │   └── vector
│   │       ├── ntm_vector_differentiation.psl
│   │       ├── ntm_vector_integration.psl
│   │       └── ntm_vector_softmax.psl
│   ├── function
│   │   ├── matrix
│   │   │   ├── ntm_matrix_logistic_function.psl
│   │   │   └── ntm_matrix_oneplus_function.psl
│   │   ├── scalar
│   │   │   ├── ntm_scalar_logistic_function.psl
│   │   │   └── ntm_scalar_oneplus_function.psl
│   │   └── vector
│   │       ├── ntm_vector_logistic_function.psl
│   │       └── ntm_vector_oneplus_function.psl
│   └── statitics
│       ├── matrix
│       │   ├── ntm_matrix_deviation.psl
│       │   └── ntm_matrix_mean.psl
│       ├── scalar
│       │   ├── ntm_scalar_deviation.psl
│       │   └── ntm_scalar_mean.psl
│       └── vector
│           ├── ntm_vector_deviation.psl
│           └── ntm_vector_mean.psl
├── ntm
│   ├── memory
│   │   ├── ntm_addressing.psl
│   │   ├── ntm_matrix_content_based_addressing.psl
│   │   └── ntm_vector_content_based_addressing.psl
│   ├── read_heads
│   │   └── ntm_reading.psl
│   ├── top
│   │   ├── ntm_interface_matrix.psl
│   │   ├── ntm_interface_top.psl
│   │   ├── ntm_interface_vector.psl
│   │   ├── ntm_output_vector.psl
│   │   └── ntm_top.psl
│   ├── trained
│   │   └── ntm_trained_top.psl
│   └── write_heads
│       ├── ntm_erasing.psl
│       └── ntm_writing.psl
├── state
│   ├── feedback
│   │   ├── ntm_state_matrix_feedforward.psl
│   │   ├── ntm_state_matrix_input.psl
│   │   ├── ntm_state_matrix_output.psl
│   │   └── ntm_state_matrix_state.psl
│   ├── outputs
│   │   ├── ntm_state_vector_output.psl
│   │   └── ntm_state_vector_state.psl
│   └── top
│       └── ntm_state_top.psl
└── trainer
    ├── differentiation
    │   ├── ntm_matrix_controller_differentiation.psl
    │   └── ntm_vector_controller_differentiation.psl
    ├── FNN
    │   ├── ntm_fnn_b_trainer.psl
    │   ├── ntm_fnn_d_trainer.psl
    │   ├── ntm_fnn_k_trainer.psl
    │   ├── ntm_fnn_trainer.psl
    │   ├── ntm_fnn_u_trainer.psl
    │   ├── ntm_fnn_v_trainer.psl
    │   └── ntm_fnn_w_trainer.psl
    └── LSTM
        ├── activation
        │   ├── ntm_lstm_activation_b_trainer.psl
        │   ├── ntm_lstm_activation_d_trainer.psl
        │   ├── ntm_lstm_activation_k_trainer.psl
        │   ├── ntm_lstm_activation_trainer.psl
        │   ├── ntm_lstm_activation_u_trainer.psl
        │   ├── ntm_lstm_activation_v_trainer.psl
        │   └── ntm_lstm_activation_w_trainer.psl
        ├── forget
        │   ├── ntm_lstm_forget_b_trainer.psl
        │   ├── ntm_lstm_forget_d_trainer.psl
        │   ├── ntm_lstm_forget_k_trainer.psl
        │   ├── ntm_lstm_forget_trainer.psl
        │   ├── ntm_lstm_forget_u_trainer.psl
        │   ├── ntm_lstm_forget_v_trainer.psl
        │   └── ntm_lstm_forget_w_trainer.psl
        ├── input
        │   ├── ntm_lstm_input_b_trainer.psl
        │   ├── ntm_lstm_input_d_trainer.psl
        │   ├── ntm_lstm_input_k_trainer.psl
        │   ├── ntm_lstm_input_trainer.psl
        │   ├── ntm_lstm_input_u_trainer.psl
        │   ├── ntm_lstm_input_v_trainer.psl
        │   └── ntm_lstm_input_w_trainer.psl
        └── output
            ├── ntm_lstm_output_b_trainer.psl
            ├── ntm_lstm_output_d_trainer.psl
            ├── ntm_lstm_output_k_trainer.psl
            ├── ntm_lstm_output_trainer.psl
            ├── ntm_lstm_output_u_trainer.psl
            ├── ntm_lstm_output_v_trainer.psl
            └── ntm_lstm_output_w_trainer.psl
```

54 directories, 162 files
