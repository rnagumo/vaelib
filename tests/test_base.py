import torch

import vaelib


def test_kl_batch() -> None:
    batch = 10
    x_dim = 5

    mu0 = torch.randn(batch, x_dim)
    var0 = torch.rand(batch, x_dim) + 0.01
    mu1 = torch.randn(batch, x_dim)
    var1 = torch.rand(batch, x_dim) + 0.01

    kl = vaelib.kl_divergence_normal(mu0, var0, mu1, var1)
    assert kl.size() == (batch,)
    assert (kl >= 0).all()


def test_kl_batch_num() -> None:
    batch = 10
    num_points = 8
    x_dim = 5

    mu0 = torch.randn(batch, num_points, x_dim)
    var0 = torch.rand(batch, num_points, x_dim) + 0.01
    mu1 = torch.randn(batch, num_points, x_dim)
    var1 = torch.rand(batch, num_points, x_dim) + 0.01

    kl = vaelib.kl_divergence_normal(mu0, var0, mu1, var1)
    assert kl.size() == (batch, num_points)
    assert (kl >= 0).all()


def test_kl_same() -> None:
    batch = 10
    x_dim = 5

    mu0 = torch.randn(batch, x_dim)
    var0 = torch.rand(batch, x_dim) + 0.01

    kl = vaelib.kl_divergence_normal(mu0, var0, mu0, var0)
    assert kl.size() == (batch,)
    assert (kl == 0).all()


def test_kl_divergence_normal_diff() -> None:
    batch = 10
    x_dim = 5

    delta_mu = torch.randn(batch, x_dim)
    delta_var = torch.rand(batch, x_dim) + 0.01
    var = torch.rand(batch, x_dim) + 0.01

    kl = vaelib.kl_divergence_normal_diff(delta_mu, delta_var, var)
    assert kl.size() == (batch,)
    assert (kl >= 0).all()


def test_nll_bernoulli() -> None:
    batch = 10
    x_dim = 5

    x = torch.rand(batch, x_dim)
    probs = torch.rand(batch, x_dim)

    nll = vaelib.nll_bernoulli(x, probs)
    assert nll.size() == (batch,)
    assert (nll >= 0).all()


def test_nll_logistic() -> None:
    batch = 10
    x_dim = 5

    x = torch.rand(batch, x_dim)
    probs = torch.rand(batch, x_dim)
    scale = torch.ones(batch, x_dim)

    nll = vaelib.nll_logistic(x, probs, scale)
    assert nll.size() == (batch,)
    assert (nll >= 0).all()
