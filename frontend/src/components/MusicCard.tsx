import { Track } from '@/types/music';
import Image from 'next/image';

interface MusicCardProps {
    track: Track;
}

export default function MusicCard({ track }: MusicCardProps) {
    return (
        <div className="music-card bg-white rounded-lg shadow-md p-4 transition-transform hover:transform hover:-translate-y-1">
            <div className="mb-4 relative h-48">
                <Image
                    src={track.album_art || '/placeholder.png'}
                    alt={track.name}
                    fill
                    className="object-cover rounded-lg"
                />
            </div>
            <h3 className="text-xl font-semibold mb-2">{track.name}</h3>
            <p className="text-gray-600 mb-2">{track.artist}</p>
            <p className="text-sm text-gray-500 mb-4">{track.album}</p>
            <div className="flex justify-between items-center">
                <a
                    href={track.spotify_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-500 hover:text-blue-600"
                >
                    Listen on Spotify
                </a>
                {track.preview_url && (
                    <audio controls className="w-32">
                        <source src={track.preview_url} type="audio/mpeg" />
                    </audio>
                )}
            </div>
            {track.discogs_info && (
                <div className="mt-4 pt-4 border-t">
                    <p className="text-sm text-gray-500">
                        Label: {track.discogs_info.label}
                    </p>
                    <p className="text-sm text-gray-500">
                        Format: {track.discogs_info.format}
                    </p>
                    <a
                        href={track.discogs_info.discogs_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-sm text-blue-500 hover:text-blue-600"
                    >
                        View on Discogs
                    </a>
                </div>
            )}
        </div>
    );
} 