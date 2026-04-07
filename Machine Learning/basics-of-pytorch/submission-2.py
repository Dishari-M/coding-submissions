import torch
import torch.nn

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def reshape(self, to_reshape: torch.Tensor) -> torch.Tensor:
        # torch.reshape() will be useful - check out the documentation
        res = torch.reshape(to_reshape, (-1, 2))
        return torch.round(res, decimals = 4)

    def average(self, to_avg: torch.Tensor) -> torch.Tensor:
        # torch.mean() will be useful - check out the documentation
        res = torch.mean(to_avg, dim=0)
        return torch.round(res, decimals = 4)

    def concatenate(self, cat_one: torch.Tensor, cat_two: torch.Tensor) -> torch.Tensor:
        # torch.cat() will be useful - check out the documentation
        res = torch.cat((cat_one, cat_two), dim=1)
        return torch.round(res, decimals = 4)

    def get_loss(self, prediction: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        res = torch.nn.functional.mse_loss(prediction, target)
        return torch.round(res, decimals = 4)