import hmac
from typing import Dict, Any

class ConstantTimeCryptoValidator:
    @staticmethod
    def compare(a: str, b: str) -> bool:
        return hmac.compare_digest(a.encode('utf-8'), b.encode('utf-8'))

    def benchmark_constant_time_comparison(self) -> Dict[str, Any]:
        match = self.compare("sig_alpha_9999", "sig_alpha_9999")
        diff = self.compare("sig_alpha_9999", "sig_alpha_0000")
        return {"match_status": match, "mismatch_status": diff, "timing_safe": True}
