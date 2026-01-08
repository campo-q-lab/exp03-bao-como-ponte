# Experimento 3 – BAO como Ponte
# Inferência do horizonte acústico (r_d) entre medições early e late universe
#
# Este script explora o papel das Oscilações Acústicas de Bárions (BAO) como
# elemento de ligação entre o universo primitivo (Planck/CMB) e medições
# tardias da constante de Hubble (H0), por meio de uma inferência aproximada
# do horizonte acústico (r_d).
#
# Toy model conceitual. Não executa ajuste cosmológico completo.

import numpy as np

# Horizonte acústico de referência (Planck)
rd_planck = 147.09  # Mpc
H0_planck = 67.4

# Valores late-universe de H0
H0_sh0es = 73.0
H0_cchp = 70.4

# Aproximação simples: r_d escala inversamente com H0
def infer_rd(H0_late):
    return rd_planck * (H0_planck / H0_late)

rd_sh0es = infer_rd(H0_sh0es)
rd_cchp = infer_rd(H0_cchp)

# Diferenças absolutas (aproximação)
delta_sh0es = abs(rd_sh0es - rd_planck)
delta_cchp = abs(rd_cchp - rd_planck)

# Erros combinados aproximados (valores ilustrativos)
err_rd_sh0es = 2.3
err_rd_cchp = 2.4

nsigma_sh0es = delta_sh0es / err_rd_sh0es
nsigma_cchp = delta_cchp / err_rd_cchp

print("Experimento 3 – BAO como Ponte")
print(f"r_d Planck (early): {rd_planck:.2f} Mpc")
print(f"r_d inferido SH0ES (H0=73): {rd_sh0es:.1f} → Δ = {delta_sh0es:.1f}, ~{nsigma_sh0es:.1f}σ")
print(f"r_d inferido CCHP (H0=70.4): {rd_cchp:.1f} → Δ = {delta_cchp:.1f}, ~{nsigma_cchp:.1f}σ")
print("Conclusão: BAO favorece o regime early-universe; a tensão concentra-se na calibração late.")
