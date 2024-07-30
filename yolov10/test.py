import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.randn(1, device=device)
    print(x)
else:
    print("CUDA is not available")
