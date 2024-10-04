from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Candidates, VoteTotal

# Create your views here.

#displaying all candidates
def index(request):
    candidate = Candidates.objects.order_by('-party')
    return render(request, 'polls/index.html',{'candidate':candidate})

@login_required
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidates, pk=candidate_id)
    
    # Check if the user has already voted for a candidate
    if VoteTotal.objects.filter(user=request.user).exists():
        # If the user has already voted, show an error message
        messages.error(request, f"You have already voted and cant vote again")
    else:
        # Create a new vote record for the user and candidate
        VoteTotal.objects.create(user=request.user, Name=candidate)
        
        # Increment the total votes for the candidate
        candidate.total_votes += 1
        candidate.save()

        # Add a success message
        messages.success(request, f'You have successfully voted for {candidate.Name}.')
    
    return redirect('index')  # Redirect to the homepage or another relevant page




