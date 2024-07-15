#!/usr/bin/env python3

import numpy as np
import pcl

def read_osa_file(file_path):
    # Lê o arquivo .osa e retorna os dados em um formato de ponto de nuvem
    # Isso dependerá do formato específico do seu arquivo .osa
    # Adapte este código para ler corretamente o arquivo .osa
    with open(file_path, 'r') as f:
        data = np.loadtxt(f)
    return data

def save_as_pcd(points, output_file):
    # Salva os dados de ponto de nuvem em um arquivo .pcd
    cloud = pcl.PointCloud()
    cloud.from_array(points.astype(np.float32))
    pcl.save(cloud, output_file)

# Caminho para o arquivo .osa
osa_file = '~/.ros/mapateste01.osa'
# Caminho para o arquivo .pcd de saída
pcd_file = '~/catkin_ws/src/tcc_marcus_albano/tcc_tello/output_file.pcd'

# Lê o arquivo .osa
points = read_osa_file(osa_file)
# Salva como .pcd
save_as_pcd(points, pcd_file)
