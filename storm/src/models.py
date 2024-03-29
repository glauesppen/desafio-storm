# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Ator(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    imagem = models.ImageField(upload_to='atores/imagens/', verbose_name='Imagem', default='atores/imagens/no_image.png')
    pais = models.CharField(max_length=150, verbose_name='País')

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
    
    def __unicode__(self):
        return self.nome

    def get_filmes_relacionados(self):
        return Filme.objects.filter(
            atores=self
        )[:20]

    def get_absolute_url(self):
        return '/ator/%i/' % self.pk


class Genero(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return '/?genero=%s' % self.pk


class Filme(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    sinopse = models.TextField(verbose_name='Sinopse')
    imagem = models.ImageField(upload_to='filmes/imagens/', verbose_name='Imagem', default='filmes/imagens/no_image.png')
    atores = models.ManyToManyField(Ator, verbose_name='Atores')
    generos = models.ManyToManyField(Genero, verbose_name='Generos')

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __unicode__(self):
        return self.nome

    def get_filmes_relacionados(self):
        return Filme.objects.filter(
            atores=self.atores.all(),
            generos=self.generos.all(),
        ).exclude(
            pk=self.pk
        )[:10]


