<p align="center">
  <img src="assets/header.svg" width="100%" alt="Runguo Li — ML Systems for Large Models">
</p>

<p align="center">
  <img src="assets/typing.svg" alt="Streaming MoE experts from disk to GPU · Compressing KV caches for long chain-of-thought · Fixing kernels in PyTorch, vLLM, Triton and LLVM · Applying to Ph.D. programs for Fall 2028">
</p>

<p align="center">
  <a href="https://runguoli.com"><img src="https://img.shields.io/badge/runguoli.com-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"></a>
  <a href="https://scholar.google.com/citations?user=t82uTeYAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar"></a>
  <a href="https://orcid.org/0009-0002-0832-6227"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"></a>
  <a href="https://runguoli.com/files/RunguoLi-ML-Systems-Resume.pdf"><img src="https://img.shields.io/badge/CV-PDF-EC1C24?style=for-the-badge&logo=readthedocs&logoColor=white" alt="CV"></a>
  <a href="mailto:runguo.ai@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

### 👋 About me

- 🎓 M.S. in Information Science at **UIUC**, applying to **Ph.D. programs in ML systems for Fall 2028**.
- ⚙️ I work between the model and the machine: MoE inference and expert streaming, KV-cache compression, distributed training and RL rollout, GPU compilers and kernels.
- 🔬 Upstream-first: reproduce the failure in the real stack, fix it there, and ship the regression test with before/after numbers.

### 🛠️ Merged upstream — 21 PRs across 13 projects

<p align="center">
  <a href="https://github.com/pytorch/pytorch/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"></a>
  <a href="https://github.com/vllm-project/vllm/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/vLLM-30A2FF?style=for-the-badge" alt="vLLM"></a>
  <a href="https://github.com/llvm/llvm-project/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/LLVM-262D3A?style=for-the-badge&logo=llvm&logoColor=white" alt="LLVM"></a>
  <a href="https://github.com/deepspeedai/DeepSpeed/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/DeepSpeed-0078D4?style=for-the-badge" alt="DeepSpeed"></a>
  <a href="https://github.com/jax-ml/jax/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/JAX-5E97F6?style=for-the-badge" alt="JAX"></a>
  <a href="https://github.com/sgl-project/sglang/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/SGLang-F5A623?style=for-the-badge" alt="SGLang"></a>
  <a href="https://github.com/Dao-AILab/flash-attention/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/FlashAttention-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="FlashAttention"></a>
  <br>
  <a href="https://github.com/triton-lang/triton/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/Triton-6E40C9?style=for-the-badge" alt="Triton"></a>
  <a href="https://github.com/apache/tvm/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/Apache_TVM-D22128?style=for-the-badge&logo=apache&logoColor=white" alt="Apache TVM"></a>
  <a href="https://github.com/verl-project/verl/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/verl-7C3AED?style=for-the-badge" alt="verl"></a>
  <a href="https://github.com/LMCache/LMCache/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/LMCache-0EA5E9?style=for-the-badge" alt="LMCache"></a>
  <a href="https://github.com/vllm-project/vllm-omni/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/vLLM--Omni-1D4ED8?style=for-the-badge" alt="vLLM-Omni"></a>
  <a href="https://github.com/JustVugg/colibri/pulls?q=is%3Apr+author%3ALiRunGuo"><img src="https://img.shields.io/badge/colibri-10B981?style=for-the-badge" alt="colibri"></a>
</p>

#### ⚡ Inference and serving

| Project | What I fixed | PR |
| --- | --- | --- |
| **vLLM** | int4 per-token-head KV cache now runs on head sizes that are not powers of two (Phi-3, head = 96) instead of aborting engine startup | [#56198](https://github.com/vllm-project/vllm/pull/56198) |
| **SGLang** | a failing DeepEP import-time host check no longer kills every server process, including dense models that never use DeepEP | [#40671](https://github.com/sgl-project/sglang/pull/40671) |
| **FlashAttention** | SM90 forward tile fitted to the block-sparse block size (8 → 32 of 40 configurations work); causal mask skipped on unmasked KV blocks (580 → 477 instructions per loop) | [#2903](https://github.com/Dao-AILab/flash-attention/pull/2903) · [#2904](https://github.com/Dao-AILab/flash-attention/pull/2904) |
| **vLLM-Omni** | block-sparse attention in the Qwen2.5-Omni Token2Wav DiT, replacing a dense mask over 4,000 keys (DiT 10.8 s → 2.87 s); a stray audio placeholder is rejected instead of crashing the engine | [#7975](https://github.com/vllm-project/vllm-omni/pull/7975) · [#7959](https://github.com/vllm-project/vllm-omni/pull/7959) |
| **LMCache** | the allocator rejects invalid sizes instead of silently emptying the cache; lazy `%`-format logging enforced | [#5117](https://github.com/LMCache/LMCache/pull/5117) · [#5125](https://github.com/LMCache/LMCache/pull/5125) |
| **colibri** | multi-drive expert streaming for the 510 GB DeepSeek-V4.1 container; OpenMP team sizing in four engines that were 18.7× slower without it; plan and engine made to agree | [#1522](https://github.com/JustVugg/colibri/pull/1522) · [#1517](https://github.com/JustVugg/colibri/pull/1517) · [#1526](https://github.com/JustVugg/colibri/pull/1526) |

#### 🧩 Compilers and frameworks

| Project | What I fixed | PR |
| --- | --- | --- |
| **PyTorch** | int32 overflow in the `cdist` CUDA backward kernel, where indices wrapped negative past 2³¹ into an illegal memory access | [#198452](https://github.com/pytorch/pytorch/pull/198452) |
| **LLVM** | ValueTracking proves `x != y` from any condition on `x - y` that excludes zero (Alive2-verified); the Attributor's `AAPointerInfo` tracked non-pointer casts as pointers and asserted at PHIs, and now follows only address-space casts | [#225200](https://github.com/llvm/llvm-project/pull/225200) · [#225290](https://github.com/llvm/llvm-project/pull/225290) |
| **JAX** | `jax.scipy.linalg.lu` accepts the batched `(..., M, N)` inputs its documentation promises | [#40931](https://github.com/jax-ml/jax/pull/40931) |
| **Triton** | nested-loop fusion trusted an `llvm.assume` outside the loop and dropped a zero-trip guard; fp64 `atomic_xchg` on AMD buffer atomics crashed codegen | [#11521](https://github.com/triton-lang/triton/pull/11521) · [#11904](https://github.com/triton-lang/triton/pull/11904) |
| **Apache TVM** | ONNX Hardmax lowers when the reduced axis has a symbolic extent | [#20416](https://github.com/apache/tvm/pull/20416) |

#### 🏋️ Training and RL post-training

| Project | What I fixed | PR |
| --- | --- | --- |
| **DeepSpeed** | ZeRO-3 rollout deadlock from unsynchronized generation stopping; Hybrid Engine falls back on unsupported architectures (H200, MI250) | [#8264](https://github.com/deepspeedai/DeepSpeed/pull/8264) · [#8265](https://github.com/deepspeedai/DeepSpeed/pull/8265) |
| **verl** | FSDP value-head critic loading restored after TRL relocated its value-head classes | [#7625](https://github.com/verl-project/verl/pull/7625) |

Every fix ships with a reproducer or regression test. Write-ups for each one are in the [portfolio](https://runguoli.com/portfolio/).

### 📝 Papers

- **BreadthKV** — [*Spend Bytes on Breadth: Precision–Count Trade-offs for Decode-Time KV Compression in Long Chain-of-Thought Reasoning*](https://arxiv.org/abs/2610.05685) — single author, arXiv 2026
- **FinVault** — [*Benchmarking Financial Agent Safety in Execution-Grounded Environments*](https://arxiv.org/abs/2601.07853) — co-first author, arXiv 2026
- **RVCFT** — [*Reasoning-Visual Critical Token Fine-Tuning for Multimodal Reasoning*](https://runguoli.com/publication/2026-07-rvcft) — co-first author, under review at AAAI 2027
- **VeriBRT** — [*Plan-Guided, Evidence-Based Automated Bug Reproduction*](https://runguoli.com/publication/2026-07-veribrt) — co-first author, under review at ICSE 2027

### 🧰 Building

- [**ARH — AI Research Helper**](https://github.com/LiRunGuo/Arhelper): a CLI-first research assistant agent with tool use, plan/execute safety, three-layer memory, skill self-learning and multi-LLM fallback.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LiRunGuo/LiRunGuo/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/LiRunGuo/LiRunGuo/output/github-contribution-grid-snake.svg">
    <img alt="Contribution graph eaten by a snake" src="https://raw.githubusercontent.com/LiRunGuo/LiRunGuo/output/github-contribution-grid-snake.svg">
  </picture>
</p>
