# Adversarial Patch Attack with Python

First, Experimenting Effects of Adversarial Patch(arXiv:1712.09665) Attacks to below `targets`.

- Target `Networks`

  - `ResNet50`
  - `ResNet101`
  - `VGG16`
  - `VGG19_with_bn`
  - `GoogLeNet`
  - `Inception_v3`

- Target `DataSets`

  - `ImageNet1k`
  - `mpii_human_pose_v1`

- Experiments
  - [x] `ResNet50` + `ImageNet1k`
  - [ ] `VGG16` + `mpii_human_pose_v1`

<br>

Second, Build `semi-automatic patch generator and evaluator`.

<br>

---

<br>

## Code Conventions

> Commit Convention: `Udacity Style`  
> https://udacity.github.io/git-styleguide/

> DocString Convention: `Google Style`  
> https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

<br>

---

<br>

## Getting Start

<br>

> Environments

| Env        | compare | Package/Version |
| ---------- | ------- | --------------- |
| `Terminal` | `==`    | `Git Bash`      |
| `Python`   | `>`     | `3.7`           |
| `Windows`  | `>`     | `10`            |

<br>

> Scripts for Start

1. `git clone https://github.com/PresentJay/Adversarial_Patch_Attack_With_Pytorch.git`
2. `cd ./Adversarial_Patch_Attack_With_Pytorch`

### [Using Virtualenv]

1. `pip install virtualenv`
2. `virtualenv venv`
3. `. venv/scripts/activate`

#### then, {venv} environment is activated.

4. `pip install -r requirements.txt`
5. `python main.py`

<br>

---

## Contact

- Present Jay (정현재)

  - **Email**: [presentj94@gmail.com](mailto:presentj94@gmail.com)
