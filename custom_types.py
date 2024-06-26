"""
Custom types for implementing voting decisions. 
"""

from typing import TypedDict, Optional
from dataclasses import dataclass

@dataclass
class UserNFTs(TypedDict, total = False):
    """
    Class for recording which NFTs a User has. 
    """
    NFTREP_V1: Optional[int]
    SPEAKER_ETHCC_PARIS23: Optional[int]
    STUDY_GROUP_HOST_C2_22_23: Optional[int]
    ETHCC_23: Optional[int]
    FUND_AUTHOR: Optional[int]
    STUDY_GROUP_HOST_360_22: Optional[int]
    STUDY_GROUP_HOST_FUND_22_23: Optional[int]
    SPEAKER_BARCAMP_PARIS_23: Optional[int]
    BARCAMP_PARIS_23: Optional[int]
    TEAM_BARCAMP_PARIS_23: Optional[int]
    FUND_MOD1: Optional[int]
    FUND_MOD2: Optional[int]
    FUND_MOD3: Optional[int]
    FUND_MOD4: Optional[int]
    FUND_MOD5: Optional[int]
    FELLOWSHIP_COMM: Optional[int]
    STUDY_SEASON_SPEAKER: Optional[int]
    STUDY_SEASON_REGISTRATION: Optional[int]
    LIVE_TRACK_1: Optional[int]
    LIVE_TRACK_2: Optional[int]
    LIVE_TRACK_3: Optional[int]
    LIVE_TRACK_4: Optional[int]
    LIVE_TRACK_5: Optional[int]
    LIVE_TRACK_6: Optional[int]
    LIVE_TRACK_7: Optional[int]
    LIVE_TRACK_8: Optional[int]
    
@dataclass
class NFTWeights(TypedDict, total = False):
    """
    Class for recording which NFTs a User has. 
    """
    NFTREP_V1: Optional[float]
    SPEAKER_ETHCC_PARIS23: Optional[float]
    STUDY_GROUP_HOST_C2_22_23: Optional[float]
    ETHCC_23: Optional[float]
    FUND_AUTHOR: Optional[float]
    STUDY_GROUP_HOST_360_22: Optional[float]
    STUDY_GROUP_HOST_FUND_22_23: Optional[float]
    SPEAKER_BARCAMP_PARIS_23: Optional[float]
    BARCAMP_PARIS_23: Optional[float]
    TEAM_BARCAMP_PARIS_23: Optional[float]
    FUND_MOD1: Optional[float]
    FUND_MOD2: Optional[float]
    FUND_MOD3: Optional[float]
    FUND_MOD4: Optional[float]
    FUND_MOD5: Optional[float]
    FELLOWSHIP_COMM: Optional[float]
    STUDY_SEASON_SPEAKER: Optional[float]
    STUDY_SEASON_REGISTRATION: Optional[float]
    LIVE_TRACK_1: Optional[float]
    LIVE_TRACK_2: Optional[float]
    LIVE_TRACK_3: Optional[float]
    LIVE_TRACK_4: Optional[float]
    LIVE_TRACK_5: Optional[float]
    LIVE_TRACK_6: Optional[float]
    LIVE_TRACK_7: Optional[float]
    LIVE_TRACK_8: Optional[float]

# Voter was designed by Joan. 
# TOODO: Be sure to give credit. 
class Voter:

    def __init__(self, vote = None, nfts = [], hasTeaAccount = True, hasWalletConnected = True, isCandidate = False):

        # The candidate that the voter prefers.
        self.vote = vote

        # List of NFTs that this voter holds.
        self.nfts = nfts 

        # Voter has an TEA account. Must be True to participate in voting.
        self.hasTeaAccount = hasTeaAccount

        # Voter has connected their wallet. Must be true to participate in voting.
        self.hasWalletConnected = hasWalletConnected

        # Candidates are not allowed to vote (?)
        self.isCandidate = isCandidate
        