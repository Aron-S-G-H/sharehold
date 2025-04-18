from django.shortcuts import render
from rest_framework.response import Response
from django.core.cache import cache
from .models import Shareholdershistory
from .serializers import ShareholderSerializer
from rest_framework.views import APIView
from .documents import ShareholderDocument


def index(request):
    return render(request, 'index.html')


class ShareholderListView(APIView):
    def get(self, request):
        symbol = request.query_params.get('symbol')
        if not symbol:
            return Response({"error": "نماد بورسی وارد نشده است"})

        cache_key = f"share_{symbol}"
        result = cache.get(cache_key)

        if not result:
            print('no result')
            s = ShareholderDocument.search().query("match", symbol=symbol)
            es_result = s.execute()
            if es_result.hits:
                print('no hit')
                result = [
                    {
                        "symbol": hit.symbol,
                        "shareholder_name": hit.shareholder_name,
                        "shareholder_percentage": hit.shareholder_percentage,
                    }
                    for hit in es_result
                ]
            else:
                shares = Shareholdershistory.objects.filter(symbol=symbol).order_by("shareholder_percentage")
                if shares.exists():
                    result = ShareholderSerializer(shares, many=True).data
            if result:
                cache.set(cache_key, result, timeout=300)

        return Response(result if result else {'error': 'نماد یافت نشد'})
