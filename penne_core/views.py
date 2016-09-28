from django.shortcuts import (
        render,
        get_object_or_404,
)

import frontdesk


def package_report(request):
    show_deposit = request.GET.get('show', None)

    deposits = frontdesk.models.Deposit.objects.order_by('-created')[:10]
    if show_deposit:
        detailed_deposit = get_object_or_404(
            frontdesk.models.Deposit, pk=show_deposit)
    else:
        detailed_deposit = frontdesk.models.Deposit.objects.order_by(
                '-created').first()

    context = {'deposits': deposits, 'detailed_deposit': detailed_deposit}
    return render(request, 'penne_core/package_report.html', context)
