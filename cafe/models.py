from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cafe(models.Model):
	class Meta:
		verbose_name = "카페"

	# 카페 이름
	name = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="카페 이름")

	# 카페 주소
	address = models.CharField(null=False, blank=False, default="", verbose_name="카페 주소")

	# 카페 등록여부
	is_registered = models.BooleanField("Cafe status", null=False, default=False, verbose_name="카페 등록여부")


class Review(models.Model):
	class Meta:
		verbose_name = "리뷰"
	
	# Cafe - Review 1:n 관계
	related_cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=False, blank=False, verbose_name="대상 카페")

    # 별점(청결도)
	score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3, verbose_name="카페 별점")

    # 패스워드
	password = models.CharField(null=False, blank=False, default="", verbose_name="카페 비밀번호")