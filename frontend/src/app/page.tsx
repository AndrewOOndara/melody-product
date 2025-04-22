'use client';

import { useState } from 'react';
import MusicCard from '@/components/MusicCard';
import { Track } from '@/types/music';

export default function Home() {
    const [prompt, setPrompt] = useState('');
    const [email, setEmail] = useState('');
    const [results, setResults] = useState<Track[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleSearch = async () => {
        if (!prompt) return;
        
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });
            
            const data = await response.json();
            if (response.ok) {
                setResults(data.results);
            } else {
                setError(data.error || 'An error occurred');
            }
        } catch (err) {
            setError('Failed to connect to the server');
        } finally {
            setLoading(false);
        }
    };

    const handleSubscribe = async () => {
        if (!email) return;
        
        try {
            const response = await fetch('/api/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email }),
            });
            
            const data = await response.json();
            if (response.ok) {
                alert(data.message || 'Successfully subscribed!');
                setEmail('');
            } else {
                alert(data.error || 'Failed to subscribe');
            }
        } catch (err) {
            alert('Failed to connect to the server');
        }
    };

    return (
        <main className="min-h-screen bg-white">
            <div className="container mx-auto px-4 py-8">
                <header className="text-center mb-12">
                    <h1 className="text-4xl font-bold text-gray-800 mb-4">
                        Melody Product
                    </h1>
                    <p className="text-xl text-gray-600">
                        Search for music using natural language
                    </p>
                </header>

                <div className="max-w-2xl mx-auto mb-8">
                    <div className="flex flex-col space-y-4">
                        <textarea
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            className="w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-black"
                            rows={4}
                            placeholder="Describe the type of music you're looking for..."
                        />
                        <button
                            onClick={handleSearch}
                            disabled={loading}
                            className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition-colors disabled:bg-blue-300"
                        >
                            {loading ? 'Searching...' : 'Search'}
                        </button>
                    </div>
                </div>

                {error && (
                    <div className="max-w-2xl mx-auto mb-8 p-4 bg-red-100 text-red-700 rounded-lg">
                        {error}
                    </div>
                )}

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {results.map((track) => (
                        <MusicCard key={track.id} track={track} />
                    ))}
                </div>

                <div className="fixed bottom-0 left-0 right-0 bg-white border-t p-4">
                    <div className="max-w-2xl mx-auto">
                        <div className="flex items-center space-x-4">
                            <input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="flex-1 p-2 border rounded-lg"
                                placeholder="Enter your email for beta updates"
                            />
                            <button
                                onClick={handleSubscribe}
                                className="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition-colors"
                            >
                                Subscribe
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
